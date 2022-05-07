#include <iostream>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t answer = 0;

        for (auto i = 0; i < 32; ++i) {
            uint32_t t = (0x1 << i);
            if (n & t > 0) {
                answer += (0x1 << (32-i-1));
            }
            std::cout <<"n = " <<n <<std::endl;
            std::cout <<"t = " <<t <<std::endl;
            //std::cout <<"n&t = " <<n&t <<std::endl;
            std::cout <<"answer = " <<answer <<std::endl;
        }
        return answer;
    }
};

int main() {
  Solution s;

  std::cout <<s.reverseBits(43261596) <<std::endl;
}
