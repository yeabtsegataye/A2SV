class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate positive and negative integers
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]

        # Rearrange the array by alternating positive and negative integers
        rearranged = []
        for pos, neg in zip(positives, negatives):
            rearranged.extend([pos, neg])

        # Append any remaining element
        if len(positives) > len(negatives):
            rearranged.append(positives[-1])
        elif len(negatives) > len(positives):
            rearranged.append(negatives[-1])

        # Ensure the first element is positive
        if rearranged[0] < 0:
            for i in range(1, len(rearranged)):
                if rearranged[i] > 0:
                    rearranged[0], rearranged[i] = rearranged[i], rearranged[0]
                    break

        return rearranged
