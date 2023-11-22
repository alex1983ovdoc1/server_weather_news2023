# from fabric import Connection
# from invoke import task

# @task
# def test(c):
#     conn = Connection(host='34.82.228.195', user='bondar1983ovdoc1', connect_kwargs={"key_filename": "C:/.ssh/id_rsa"})
#     conn.run('date')
#     conn.local('date')




from fabric.api import env, settings, run, local, cd, sudo

env.hosts = ["34.82.228.195"]
env.user = "bondar1983ovdoc1"
# env.key_filename = "C:/.ssh/id_rsa"

def test():
    with settings(connect_kwargs={"key_filename": "C:/.ssh/id_rsa"}, warn_only=True):
        run("date")
        local("date")

def update():
	with cd("/home/bondar1983ovdoc1/server_weather_news2023"):		
		run("git pull")
		sudo("supervisorctl restart flask")

	# with settings(sudo_prompt="Password:", warn_only=True):
	# 	cd("/home/bondar1983ovdoc1/server_weather_news2023")
	# 	run("git pull")
	# 	sudo("supervisorctl restart flask")




# from fabric.api import *

# env.hosts = ["34.82.228.195"]
# env.user = "bondar1983ovdoc1"
# # env.reject_unknown_hosts = False
# # env.disable_known_hosts = True

# def test():
# 	# with settings(connect_kwargs={"key": key}, warn_only=True):
# 	# 	run("date")
# 	# 	local("date")
#     with settings(connect_kwargs={"key_filename": "C:/.ssh/id_rsa"}, warn_only=True):
#         run("date")
#         local("date")