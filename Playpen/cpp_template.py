
build_template = """
cc_binary(
    name = 'main',
    srcs = [
        'Main.cc'
    ]
)
"""

file_content = """
#include <iostream>

int main(int argc, char const *argv[])
{
    std::cout << "### START ### << std::endl;

    std::cout << "### END ### << std::endl;
    return 0;
}

"""