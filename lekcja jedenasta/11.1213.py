import random

class Arrays(): 
    @staticmethod 
    def print_in_col(array): 
        for c in array: 
            print(c) 

    @staticmethod
    def put_commas(array):
        array1 = [str(element) for element in array]
        print(','.join(array1))
    
    @staticmethod
    def same_value_list(elements_num, element_value):
        list = []
        for x in range(elements_num):
            list.append(element_value)

        return list

    @staticmethod
    def random_list_generator(elements_num, range_1, range_2):
        list = []
        for x in range(elements_num):
            list.append(random.randint(range_1, range_2))
        
        return list
    
    @staticmethod
    def num_of_elements_in_range(array, value_from, value_to):
        
        counter = 0
        
        for x in array:
            for y in range(value_from, value_to+1):
                if x==y:
                    counter+=1
        
        return counter
                

my_array = [4,1,8,7,2] 
Arrays.print_in_col(my_array)
Arrays.put_commas(my_array)
print(Arrays.same_value_list(10,4))
print(Arrays.random_list_generator(20,-7,8))

my_array2 = [2,1,-1,543,123,5765,1231,123,0]

print(Arrays.num_of_elements_in_range(my_array2, -1, 1))