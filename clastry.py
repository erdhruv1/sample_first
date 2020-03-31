
class Abc
    {
        private:
            int a = 2

        public:
            void display()
            {
                cout<<"Hi";
            }
    }

int main()
    {
        Abc abcObj;
        *(Abc::ptr) = &(Abc::a)

        *Abc::ptr = &Abc::a

        cout<<"Value of a is: %d"<<*(Abc::ptr)
        return 0;
    }