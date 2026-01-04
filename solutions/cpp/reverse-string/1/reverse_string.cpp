#include "reverse_string.h"
#include <iostream>

namespace reverse_string
{
  std::string reverse_string(std::string toReverse)
  {
    std::string result = "";
    for (std::string::size_type i = toReverse.length(); i > 0; i--)
    {
      result.push_back(toReverse.at(i - 1));
    }
    std::cout << result;
    return result;
  }
}

// for debugging
// int main()
// {
//   std::string result = reverse_string::reverse_string("abcdefghijk");
//   return 0;
// }
