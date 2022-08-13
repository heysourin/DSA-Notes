
#! binary search is used for sorted arrays
# ? Sorted array means: either ascending or decending order
# ? eg: [-14,-7,-1,2,4,8,12,15,19,22,30]


#! Algorithm:
#1. find the middle element
#2. check < or > than middle element, if larger search right side, if smaller search left side
#3. if the middle element == target element, its ans
#4. otherwise do the same in the left or right side
#5. start point will be the right next elemnent of the middle element
