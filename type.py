class TypeRegistry:
    def __init__(self):
        self._type_dict = {  }
        
    def Add(self, type):
        if type.name not in self._type_dict:
            self._type_dict[type.name] = type
            
    def Get(self, type):
        if type.name in self._type_dict:
            return self._type_dict[type.name]
        else:
            return None

class Type:
    def __init__(self, name):
        self.name = name
        
    def IsImportRequired(self):
        raise TypeError()
        
    def ImportFile(self):
        raise TypeError()
                
class BaseType(Type):
    def __init__(self, name, is_signed, n_bytes, is_float):
        Type.__init__(self, name)
        self.is_signed
        self.n_bytes
        self.is_float
        
    def IsImportRequired(self):
        return False
        
    def ImportFile(self):
        return None
        
class AliasType(Type):
    def __init__(self, name, alias, import_file):
        Type.__init__(self, name)
        self.alias = alias
        self.import_file = import_file
        
    def IsImportRequired(self):
        return True
        
    def ImportFiles(self):
        return self.import_file
        
class ComplexType(Type):
    def __init__(self, name, base_type, attributes, methods):