# microservices-unit-tests

Unit test for each pusblished Clear micro service

# How to use:
###  make update
This step will update all the docker images, including the offical ones and clearlinux ones.

### make status
This step will show the docker images size information, also the clearlinux version of the clear docker image.

### make tests
This step will run all the test cases one by one.

# How to contribute:
If you want to add one more test case, for example, to test micro service nginx.
You need create a nginx folder, and add the test script entry in the file nginx/nginx.sh.
Then above mentioned steps 1~3 will handle the test flow.
