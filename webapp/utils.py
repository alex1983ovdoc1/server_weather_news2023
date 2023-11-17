from urllib.parse import urlparse, urljoin
from flask import request


# examenation url, where send users (is my url)
def is_safe_url(target):
	ref_url = urlparse(request.host_url)
	test_url = urlparse(urljoin(request.host_url, target))
	return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

# examenation url have 'next', referrer
def get_redirect_target():
	for target in request.values.get('next'), request.referrer:
		if not target:
			continue
		if is_safe_url(target):	
			
			list_url = ['http://127.0.0.1:5000/users/login', 'http://127.0.0.1:5000/users/login?next=/users/register?', 'http://127.0.0.1:5000/admin', 'http://127.0.0.1:5000/admin/?next=/?']		
			if target in list_url:
				target = 'http://127.0.0.1:5000/'				 

			return target