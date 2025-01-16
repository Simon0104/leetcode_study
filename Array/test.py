# 定义变量
Y = cp.Variable((n, n))  # 变量矩阵 Y
A = np.random.randn(N * n, n)  # 矩阵 A 的常量部分

# 构造 LMI 矩阵
LMI_matrix = cp.bmat([
    [cp.kron(np.eye(N), Y), A],
    [A.T, -np.eye(n)]
])
