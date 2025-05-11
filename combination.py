class Combination:
    '''
    二項係数（nCk）を@param:modで割った余りを求める
    @pram N
    @pram mod 
    '''
    def __init__(self, N, mod):
        self.N = N
        self.mod = mod

        self.fac = [-1] * N
        self.fac_inv = [-1] * N
        self.inv_ele = [-1] * N

        self.fac[0], self.fac[1] = 1, 1
        self.fac_inv[0], self.fac_inv[1] = 1, 1
        self.inv_ele[1] = 1

        for i in range(2, N):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv_ele = (self.mod
                            - self.inv_ele[self.mod % i] * (self.mod / i)
                            ) % self.mod
            self.fac_inv[i] = self.fac_inv[i - 1] * self.inv_ele[i] % self.mod

    def comb(self, n, k):
        if k > n:
            return 0
        return (self.fac[n] * self.fac_inv[k] * self.fac_inv[n - k]) % self.mod
