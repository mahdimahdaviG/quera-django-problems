from django.http import JsonResponse

from .models import Book, Borrowing
from django.contrib.auth.models import User

# DONE
def get_book_users(request, book_id):
    borrowings = Borrowing.objects.filter(book__id=book_id)

    response = []
    
    for b in borrowings:
        j = {'username': b.user.username, 'date': b.date.isoformat()}
        response.append(j)

    return JsonResponse(response, safe=False)

def borrow_book(request, book_id, user_name):
    status_code = -1

    try:
        user = User.objects.get(username=user_name)
        book = Book.objects.get(id=book_id)

        if book.user_borrowed is not None:
            status_code = 1
        else:
            if user.book_set.count() != 0:
                status_code = 2
            else:
                book.borrow_book(user)
                status_code = 0

    except User.DoesNotExist:
        status_code = 3
    except Book.DoesNotExist:
        status_code = 3
    except:
        status_code = 4

    return JsonResponse({'status': status_code})

# DONE
def return_book(request, book_id):
    status_code = 3

    try:
        book = Book.objects.get(id=book_id)

        if book.user_borrowed is None:
            status_code = 1
        else:
            book.return_book()
            status_code = 0
    except Book.DoesNotExist:
        status_code = 2

    return JsonResponse({'status': status_code})
