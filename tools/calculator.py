import ast
import operator

# Supported operations
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}
def evaluate(node):
    # Number
    if isinstance(node, ast.Constant):
        return node.value

    # Binary operations (+, -, *, /, %, **)
    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)

        operator_func = OPERATORS[type(node.op)]

        return operator_func(left, right)

    # Unary operations (-5)
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate(node.operand)

        operator_func = OPERATORS[type(node.op)]

        return operator_func(operand)

    else:
        raise ValueError("Unsupported operation.")
def calculate(expression: str) -> str:
    try:
        # Parse the expression into an AST
        tree = ast.parse(expression, mode="eval")

        # Evaluate the expression safely
        result = evaluate(tree.body)

        return str(result)

    except Exception as e:
        return f"Calculator Error: {e}"