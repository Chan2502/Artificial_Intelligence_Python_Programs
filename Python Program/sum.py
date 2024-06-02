class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        max1=max(salary)
        min1=min(salary)
        sum=0
        for i in range(0,len(salary)):
            if(salary[i]!=max1 or salary[i]!=max1):
                sum=sum+salary[i]
        return (sum/2)

