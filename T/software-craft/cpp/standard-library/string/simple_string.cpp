#include <iostream>
#include <cstring>

using namespace std;

class String
{
public:
    String();
    ~String();

    String(const char *);
    String(String &);
    String& operator = (String &);
    char * c_str();
    size_t size();

private:
	char *_str;
	size_t _size;
};

String::String():
    _str(NULL),
    _size(0)
{

}

String::~String()
{
	if (NULL != _str)
    {
        delete [] _str;
        _str = NULL;
    }
    _size = 0;
}

String::String(const char *s)
{
	if (NULL == s)
    {
        _str = NULL;
        _size = 0;
        return;
    }

    _size = strlen(s);
    _str = new char[_size + 1];
    strcpy(_str, s);
}

String::String(String& s)
{
	_size = s.size();
	_str = new char [s.size() + 1];
	strcpy(_str, s.c_str());
}

String& String::operator= (String& s)
{
    if (this != &s)
    {
        _size = s.size();
        _str = new char [_size + 1];
        strcpy(_str, s.c_str());
    }
	return *this;
}

size_t String::size()
{
	return _size;
}

char* String::c_str()
{
	return _str;
}


int main()
{
    String str("my word");
    cout << str.c_str() << endl;

    return 0;
}
