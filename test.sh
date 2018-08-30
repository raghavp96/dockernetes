echo "Creating test environment...."
mkdir test

cp app.py test/app.py
cp Makefile test/Makefile
cp testfiles/config.json test/config.json

cd test
mkdir FolderOne
mkdir FolderTwo

cp ../testfiles/Dockerfile FolderOne/Dockerfile
cp ../testfiles/Dockerfile FolderTwo/Dockerfile
cp ../testfiles/flaskapp.py FolderOne/flaskapp.py
cp ../testfiles/flaskapp.py FolderTwo/flaskapp.py

echo "********************************************************"
echo "Building and starting test containers and attaching them to the Docker network"
echo ""
make start
sleep 15
echo "********************************************************"
echo "Listing ongoing Docker processes (running containers)..."
echo ""
docker ps -a
echo "********************************************************"
echo "Listing Docker networks..."
echo ""
docker network ls
echo "********************************************************"
echo "Stopping and deleting containers and removing the Docker network"
make stop

cd .. && rm -rf test