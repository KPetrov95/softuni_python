def operate(operator, *args):

    def summarize(*nums):
        return sum(nums)

    def subtract(*nums):
        result = nums[0]

        for el in nums[1:]:
            result -= el
        return result

    def divide(*nums):
        result = nums[0]
        for el in nums[1:]:
            result /= el
        return result

    def multiply(*nums):
        result = nums[0]
        for el in nums[1:]:
            result *= el
        return result

    mapper = {"+": summarize,
              "-": subtract,
              "/": divide,
              "*": multiply,}

    return mapper[operator](*args)
