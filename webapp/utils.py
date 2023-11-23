from urllib.parse import urlparse, urljoin
from flask import request


# examenation url, where send users (is my url)
def is_safe_url(target):
	ref_url = urlparse(request.host_url)
	test_url = urlparse(urljoin(request.host_url, target))
	return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


# ref_url = urlparse(request.host_url)
# print(ref_url)
# examenation url have 'next', referrer
def get_redirect_target():

	for target in request.values.get('next'), request.referrer:

		referrer = request.referrer
		parsed_url = urlparse(referrer)
		# print(parsed_url)

		if 'None' in str(target) and target is not None or parsed_url.path=='/users/login':
			target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"	


		if target is None:
			target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.path}"	

		if  'next' in str(parsed_url.query):
			target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"

		if '/users/register' in target:
			target = f"{parsed_url.scheme}://{parsed_url.netloc}"	

		# print(target)

		if not target:
			continue
		if is_safe_url(target):	
			list_url = ['/users/login', '/users/login?next=/users/register?', '/admin', '/admin/?next=/?', '/?', 'None', '/users/None']

			if target in list_url:
				# target = f'http://127.0.0.1:5000/'	
				# referrer = request.referrer
				# parsed_url = urlparse(referrer)
				target = f"{parsed_url.scheme}://{parsed_url.netloc}"


	return target