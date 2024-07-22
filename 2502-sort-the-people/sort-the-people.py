class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=[["",0] for _ in names]
        for i,name in enumerate(names):
            people[i][0]=name
            people[i][1]=heights[i]
        people.sort(key=lambda x:-1*x[1])
        return [person[0] for person in people]