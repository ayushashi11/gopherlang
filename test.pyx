cdef int x=0
cdef str y="hello"
cdef int func():
    print(x,y)
    return 0
cdef int main():
    print(func())
    return 0
main()