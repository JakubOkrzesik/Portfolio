from contact import Contact
from contact_list import Contact_list

info = Contact('John Brown', 'brown@onet.pl', 555234000)
addition = Contact_list()
addition.contactadd(info)
addition.contactdisplay()


