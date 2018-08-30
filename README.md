# dockernetes

Okay, so a little bit of backstory: i'm working on a project that I eventually want to take to k8s, but I'm not quite there yet. So I was thinking, why not accomplish what I want and have my microservices run in containers and talk to each other while being on the same Docker network? So I did just that! And then I thought, "Wait, I can totally make this more generic and easily configurable so that people in the same boat can do this too!" And that's what inspired dockernetes (Please tell me if the name scheme is copyright infringement and I'll remove it immediately `:)`) 

## Configure your stuff!

Provide information about the containers you are going to have running. If you have more than two, you can just add to the JSON!!!

```
{
    "Network" : {
        "Name" : "my_network_name", 
        "Containers" : [
            {
                "Folder" : "FolderOne",
                "Name" : "service_one",
                "ExternalPort" : "8001",
                "Port" : "8080"
            },
            {
                "Folder" : "FolderTwo",
                "Name" : "service_two",
                "ExternalPort" : "8002",
                "Port" : "8080"
            }
        ]
    } 
}
```

After you've configured your things, just run:

```
make start
```

and when you're done:

```
make stop
```