def isPalindrome(s: str) -> bool:
        valid_str = 'abcdeefghijklmnopqrstuvwxyz0123456789'
        valid_set = set()
        for n in range(len(valid_str)):
            valid_set.add(valid_str[n])
        formated_str=  ""
        for n in range(len(s)):
            if s[n].lower() in valid_set:
                 formated_str+=s[n]
        return formated_str == formated_str[::-1]

def isPalindrome_2(s: str) -> bool:
        valid_str = 'abcdeefghijklmnopqrstuvwxyz0123456789'
        valid_set = set()
        for n in range(len(valid_str)):
            valid_set.add(valid_str[n])
        left,right = 0, len(s)-1
        while left <right:
            while left< right and s[left].lower() not in valid_set:
                left+=1
            while left< right and s[right].lower() not in valid_set:
                 right-=1
            if left>= right:
                 break
            else:
                if s[left].lower()!= s[right].lower():
                    return False
                left +=1
                right -=1
        return True

              
print(isPalindrome_2("::::::::"))