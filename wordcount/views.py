from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] #글 자체를 받아옴.
    words = text.split()
    word_dictionary = {} #빈 사전형 자료형
    #<단어 : 횟수, 단어: 횟수>
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word] +=1
        else:
            #add to dictionary
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 
                                           'total': len(words), 
                                           'dictionary': word_dictionary.items()
                                          }
                 ) #{'key': value} 사전형 객체

def address(request):
    address_dictionary = {}
    name = request.GET['name']
    phoneNum = request.GET['phoneNumber']
    address_dictionary[name] = phoneNum
    return render(request, 'address.html',{'address_dic': address_dictionary.items()})
