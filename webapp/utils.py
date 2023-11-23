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
		print(type(target))
		print(target)

		referrer = request.referrer
		parsed_url = urlparse(referrer)
		print(parsed_url)

		# if 'None' in str(target) and target is not None:

		# 	print('1111')
		# 	# target = f"{parsed_url.scheme}://{parsed_url.netloc}"	
		# 	target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"	
		# 	# break

		# if target is None:
		# 	target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.path}"	
		# 	print('222')
		# 	# break

		# if  'next' in str(parsed_url.query):
		# 	print('333')
		# 	target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"

		# if '/users/register' in target:   or parsed_url.path=='/users/login'
		# 	target = f"{parsed_url.scheme}://{parsed_url.netloc}"
		# 	print('444')	

		if 'None' in str(target) and target is not None:
			print('1111')
			# target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"
			if 'next' in str(parsed_url.query): 				
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"
			else:
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.query}"
		
		elif target is None:
			print('222')
			target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.path}"

		elif 'login' in str(target) and 'news' not in str(target):
			print('333')
			target = f"{parsed_url.scheme}://{parsed_url.netloc}"
		
		elif 'login' in str(target) and 'news' in str(target):
			print('444')
			if 'next' in str(parsed_url.query): 				
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{str(parsed_url.query).replace('next=', '')}"
			else:
				target = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.query}"


		if not target:
			continue
		# if is_safe_url(target):	
		# 	list_url = ['/users/login', '/users/login?next=/users/register?', '/admin', '/admin/?next=/?', '/?', 'None', '/users/None']
		# 	if target in list_url:
		# 		target = f"{parsed_url.scheme}://{parsed_url.netloc}"

		print(target)

	return target