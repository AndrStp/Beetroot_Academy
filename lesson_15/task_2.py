# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

# ```
# def stop_words(words: list):
#     pass

# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
 
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
# ```


def stop_words(words: list):
    def stop_words_decorator(func):
        def wrapper(arg):
            result: str = func(arg)

            for word in words:
                if word in result:
                    modified_result = result.replace(word, '*')
            
            return modified_result
        
        return wrapper
    
    return stop_words_decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
 
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"