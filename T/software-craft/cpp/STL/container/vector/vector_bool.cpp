#include <iostream>
#include <vector>

int main()
{
    std::vector<bool> vb;

    vb.push_back(true);
    vb.push_back(false);

    std::cout <<vb.at(0) <<std::endl;
}
