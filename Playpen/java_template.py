
build_template = """
java_binary(
    name = 'main',
    main_class = 'playpen.java.Main',
    srcs = [
        'Main.java'
    ]
)
"""

file_content = """
package playpen.java;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("### START ###");

        System.out.println("### END ###");
    }
}
"""