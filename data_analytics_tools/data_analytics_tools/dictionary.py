class Dictionary(dict):

    __getattr__= dict.__getitem__
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__
    
    def add_keys(self, keys, kcopy=True):

      if type(keys) is dict:
        [self.__dict__.__setitem__(k, v) for k, v in keys.items()]
        return

      for k in keys:
        if kcopy == False:
          self.__dict__[k] = ''
        else:
          self.__dict__[k] = k

    def update_values(self, values):

      if type(values) is dict:
        [self.__dict__.__setitem__(k, v) for k, v in values.items()]
        return

      temp = list(self.__dict__)
      if len(values) > len(temp):
        return False
      for i, v in enumerate(values):
        self.__dict__[temp[i]] = v
      return True

    def update_keys(self, keys):

      if type(keys) is dict:
        for k, v in keys.items():
          self.__dict__[v] = self.__dict__[k]
          del self.__dict__[k]
        return

      temp = list(self.__dict__)
      if len(keys) > len(temp):
        return False
      for i, v in enumerate(keys):
        self.__dict__[v] = self.__dict__[temp[i]]
        del self.__dict__[temp[i]]

    def __getitem__(self, arg):
      return self.__dict__[arg]

    def clear(self):
      self.__dict__.clear()