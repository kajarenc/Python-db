import shelve 	 	
file_db = shelve.open("db")
memory_db = {}

def choose_storage(obj):    
    if str(obj).find('Image') != -1:
	    return "file"
    else:
	    return "mem"


def put(obj):
    if choose_storage(obj) == "file":
	    put_file(obj)
    else:
	    put_mem(obj)
	
def get(id):
    to_return = get_mem(id)	
    if to_return == None:
        return get_file(id)	
    
def put_file(obj):
    file_db[str(obj.get_id())] = obj
	
def get_file(id):
    to_return = None
    try:
        to_return = file_db[str(id)]
    except KeyError:
        print "Error"
    return to_return
    
def put_mem(obj):
    memory_db[obj.get_id()] = obj
	
def get_mem(id):
    to_return = None
    try:
        to_return = memory_db[id]
    except KeyError:
        print "Error"
    return to_return

class Image(object):
   id = None
   
   def __str__(self):
      return str(type(self)) + str(self.id)
   
   def get_id(self):
       return self.id

class BigInteger(object):
   id = None
   
   def __str__(self):
      return str(type(self)) + str(self.id)
   
   def get_id(self):
       return self.id

	   
a = Image()
a.id = 7
put(a)

a = BigInteger()
a.id = 8
put(a)

print get(7)	   
print get(8)	   

get(9)	   
get(9)	   
