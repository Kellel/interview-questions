# Interview questions

## Salt grain module
Create a salt execution module that returns data on all disk present on a device similar to the following:
```
'device': '/dev/sda', 
'major-device': '8', 
'blocks': '125034840', 
'minor-device': '0'
```

## Rest Cli
Create a simple cli to pull data from a 3rd party rest api (you may use any you like, but in this example I will be using https://jsonplaceholder.typicode.com/)

Example cli usage:
```
kellen@Chewbacca:~$ python rest.py --help                                                                                                                                                                                
usage: Get some data from https://jsonplaceholder.typicode.com/
       [-h] {list,get} ...

positional arguments:
  {list,get}
    list      List some posts
    get       Get a specific post

optional arguments:
  -h, --help  show this help message and exit
kellen@Chewbacca:~$ python rest.py list --help                                                                                                                                                                           
usage: Get some data from https://jsonplaceholder.typicode.com/ list
       [-h] [-n NUMBER]

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        List N Posts
kellen@Chewbacca:~$ python rest.py list -n 1
{
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto", 
    "id": 1, 
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", 
    "userId": 1
}
kellen@Chewbacca:~$ python rest.py get --help
usage: Get some data from https://jsonplaceholder.typicode.com/ get
       [-h] [-c] id

positional arguments:
  id              Get post <id>

optional arguments:
  -h, --help      show this help message and exit
  -c, --comments  Include comments
kellen@Chewbacca:~$ python rest.py get 1
{
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto", 
    "id": 1, 
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", 
    "userId": 1
}
kellen@Chewbacca~$ python rest.py get -c 1                                                                                                                                                                              
{
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto", 
    "comments": [
        {
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium", 
            "email": "Eliseo@gardner.biz", 
            "id": 1, 
            "name": "id labore ex et quam laborum", 
            "postId": 1
        }, 
        {
            "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et", 
            "email": "Jayne_Kuhic@sydney.com", 
            "id": 2, 
            "name": "quo vero reiciendis velit similique earum", 
            "postId": 1
        }, 
        {
            "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti rati
one", 
            "email": "Nikita@garfield.biz", 
            "id": 3, 
            "name": "odio adipisci rerum aut animi", 
            "postId": 1
        }, 
        {
            "body": "non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\nquia voluptas consequuntur itaque dolor\net qui rerum deleniti ut occaecati", 
            "email": "Lew@alysha.tv", 
            "id": 4, 
            "name": "alias odio sit", 
            "postId": 1
        }, 
        {
            "body": "harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et", 
            "email": "Hayden@althea.biz", 
            "id": 5, 
            "name": "vero eaque aliquid doloribus et culpa", 
            "postId": 1
        }
    ], 
    "id": 1, 
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", 
    "userId": 1
}
```

## cache-debugging-problem
A simple python debugging problem for interviews

### Goals
1. All unittests in `python debug.py` should pass
2. You should only need to modify `cache.py`
3. Execution time of `python debug.py` should be less than a second
