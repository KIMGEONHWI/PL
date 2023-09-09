import java.util.*;

public class PL2 {
    static Deque<Character> token = new LinkedList<>();
    static boolean zerodivde = true;
    static int aexpr()
    {
        int left = term();

        while(true)
        {
            if (token.size() != 0 && (token.peek() == '*' || token.peek() == '/'))
            {
                char op = token.peek();
                token.poll();

                int right = term();

                if (op == '*')
                {
                    left *= right;
                }
                else
                {
                    if (right == 0)
                    {
                        zerodivde = false;
                    }
                    else
                    {
                        left /= right;
                    }
                }
            }
            else
            {
                break;
            }
        }

        return left;
    }

    static int term()
    {
        int left = factor();

        while(true)
        {
            if (token.size() != 0 && (token.peek() == '+' || token.peek() == '-'))
            {
                char op = token.peek();
                token.poll();

                int right = factor();

                if (op == '+')
                {
                    left += right;
                }
                else
                {
                    left -= right;
                }
            }
            else
            {
                break;
            }
        }

        return left;
    }

    static int factor()
    {
        int num = 0;

        if (token.size() != 0 && '0' <= token.peek() && token.peek() <= '9')
        {
            return number();
        }
        else
        {
            token.poll();
            num = aexpr();

            token.poll();
            return num;
        }
    }

    static int number()
    {
        int num = 0;

        while (true)
        {
            if (token.size() != 0 && '0' <= token.peek() && token.peek() <= '9')
            {
                if (num == 0)
                {
                    num += dec();
                }
                else
                {
                    num *= 10;
                    num += dec();
                }
            }
            else
            {
                break;
            }
        }

        return num;
    }

    static int dec()
    {
        int num = token.peek() - '0';
        token.poll();

        return num;
    }

    public static void main(String[] args) {

        while (true)
        {
            Scanner sc = new Scanner(System.in);
            String syntax = sc.nextLine();

            if (syntax.length() == 0)
                break;

            boolean b = true;
            Stack<Integer> stack = new Stack<>();
            token.clear();
            zerodivde = true;

            //토큰화 및 syntax error 확인
            {
                for (int i = 0; i < syntax.length(); i++)
                {
                    char ch = syntax.charAt(i);

                    if (('(' <= ch && ch <= '+') || ch == '-' || ('/' <= ch && ch <= '9'))
                    {
                        if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
                        {
                            if (token.size() == 0 || token.peekLast() == '+' || token.peekLast() == '-'
                                    || token.peekLast() == '*' || token.peekLast() == '/')
                            {
                                b = false;
                                break;
                            }
                        }
                        else if (ch == '(')
                        {
                            stack.push(0);

                            if (token.size() != 0 && ('0' <= token.peekLast() && token.peekLast() <= '9'))
                            {
                                b = false;
                                break;
                            }
                        }
                        else if (ch == ')')
                        {
                            if (stack.empty())
                            {
                                b = false;
                                break;
                            }
                            else
                            {
                                stack.pop();
                            }

                            if (token.size() != 0 && token.peekLast() == '(')
                            {
                                b = false;
                                break;
                            }
                        }
                        else
                        {
                            if (token.size() != 0 && token.peekLast() == ')')
                            {
                                b = false;
                                break;
                            }
                        }

                        token.add(ch);
                    }
                    else if (ch == ' ')
                    {
                        continue;
                    }
                    else
                    {
                        b = false;
                        break;
                    }
                }

                if (stack.size() != 0)
                {
                    b = false;
                }

                if (token.size() != 0 && (token.peekLast() == '+' || token.peekLast() == '-'
                        || token.peekLast() == '*' || token.peekLast() == '/'))
                {
                    b = false;
                }
            }

            if (b)
            {
                int res = aexpr();

                if (zerodivde)
                {
                    System.out.println(res);
                }
                else
                {
                    System.out.println("can't divide 0");
                }
            }
            else
            {
                System.out.println("syntax error!");
            }
        }
    }
}