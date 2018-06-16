class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = 2 ** 31 - 1

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._min = min(x, self._min)
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self._stack.pop()
        if x == self._min:
            if len(self._stack) == 0:
                self._min = 2 ** 31 - 1
            else:
                self._min = min(self._stack)

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """

        return self._min
