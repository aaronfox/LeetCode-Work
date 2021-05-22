-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
/* Write your T-SQL query statement below */
SELECT E1.Name AS Employee
FROM Employee AS E1, Employee AS E2
WHERE E1.ManagerId = E2.Id AND E1.Salary > E2.Salary 

/* Could also use JOIN here */

-- SELECT E1.Name as Employee
-- FROM Employee as E1 JOIN Employee as E2
--     ON E1.ManagerId = E2.Id
--     AND E1.Salary > E2.Salary
