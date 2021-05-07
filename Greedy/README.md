### 贪心
- 本质为每次操作都达到局部最优，当问题有唯一最优解的时候，最终达到全局最优。
    
    *值得说明的是，"贪心"并不是"贪得无厌"，它只是指每次操作所能达到的最优极限*
> 例如：需要挪动200kg的重物，但是工具每次只能挪动100kg，最简单的方式就是直接把200kg直接挪过去，但受限于工具的极限，只能100kg 100kg挪动，所以，这个每次把100kg打满的动作，就是贪心

一般来说，当题目问题中存在最多最少等字眼，考虑是否可以采用贪心或者动态规划求解。

较为常见的三类问题 

1. 典型的贪心问题
    
    较简单，没啥技巧，做就完事了
    - [AssignCookies](./AssignCookies.py)
    - [CanPlaceFlowers](./CanPlaceFlowers.py)
    - [BestTimeToBuyAndSellStock2](./BestTimeToBuyAndSellStock2.py)
    - [NonDecreasingArray](./NonDecreasingArray.py)
    
2. 多维度优化问题
    这类问题一般有两个或更多的因素需要考虑，我们可以考虑对多个维度one by one地去解决 
    >（ps：我甚至觉得每次只解决一个维度也算贪心，也符合 局部最优->全局最优）
    
    *在解决过程中可能需要多次使用贪心，或者贪心配合其他不同思路去解决不同维度的问题*
    - [Candy](./Candy.py)
    - [QueueReconstructionByHeight](./QueueReconstructionByHeight.py)
    
3. 区间问题
    一般包括 区间合并 / 区间去重 / 区间调度等 均可以贪心算法去实现
    
    * 该类问题一般不会直接直白地告诉是区间问题，需要先将其抽象为区间。套路一般为先排序后贪心
    - [NonOverlappingIntervals](./NonOverlappingIntervals.py)
    - [MinimumNumberOfArrowsToBurstBalloons](./MinimumNumberOfArrowsToBurstBalloons.py)
    - [PartitionLabels](./PartitionLabels.py)