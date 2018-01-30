Haoji's personal website

---

* Container - Docker(ubuntu 16.04)
* Web server - Flask/uWSGI/NGINX/Supervisor
* Cache - Redis
* Database - MongoDB
* Some Google APIs:
	1.Google Map JavaScipt
	2.Google Map GeoCode
	3.Google reCaptcha

---
TODOs:

1.Make nginx talk to uwsgi - DONE
2.1.Move this repo to github
3.Enable HTTPS and turn on auto renewal:
https://certbot.eff.org/#ubuntuxenial-nginx
4.Automate docker image build
5.Automate docker image push
6.Automate deploy to EC2 instance

More TODOs:
1.Make google maps detect user location
2.Store user submissions to database
3.Split database into its own instance
4.Split cache into its own instance

---
Notes

On Ubuntu: http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php

Some MongoDB tutorials: http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_Range_Queries_Counting_Indexing.php

https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-1

decide to use S3 instead of MongoDB's GridFS, S3 is already managed and my application doesn't cost that much yet


local development:
* Install docker, docker cli, docker-compose
* `docker-compose up -d app`
* `docker exec -it app bash`
* `docker tag app:latest divid86391/noises_life:1.0.1`
* `docker push divid86391/noises_life`
