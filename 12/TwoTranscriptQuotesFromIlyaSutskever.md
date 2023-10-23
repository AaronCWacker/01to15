https://www.youtube.com/watch?v=9EN_HoEk3KY&t=172s


1:42
program the does very very well on your data then you will achieve the best
1:48
generalization possible with a little bit of modification you can turn it into a precise theorem
1:54
and on a very intuitive level it's easy to see what it should be the case if you
2:01
have some data and you're able to find a shorter program which generates this
2:06
data then you've essentially extracted all the all conceivable regularity from
2:11
this data into your program and then you can use these objects to make the best predictions possible like if if you have
2:19
data which is so complex but there is no way to express it as a shorter program
2:25
then it means that your data is totally random there is no way to extract any regularity from it whatsoever now there
2:32
is little known mathematical theory behind this and the proofs of these statements actually not even that hard
2:38
but the one minor slight disappointment is that it's actually not possible at
2:44
least given today's tools and understanding to find the best short program that 



https://youtu.be/9EN_HoEk3KY?t=442
5
to talk a little bit about reinforcement learning so reinforcement learning is a framework it's a framework of evaluating
6:53
agents in their ability to achieve goals and complicated stochastic environments
6:58
you've got an agent which is plugged into an environment as shown in the figure right here and for any given
7:06
agent you can simply run it many times and compute its average reward now the
7:13
thing that's interesting about the reinforcement learning framework is that there exist interesting useful
7:20
reinforcement learning algorithms the framework existed for a long time it
7:25
became interesting once we realized that good algorithms exist now these are there are perfect algorithms but they
7:31
are good enough to do interesting things and all you want the mathematical
7:37
problem is one where you need to maximize the expected reward now one
7:44
important way in which the reinforcement learning framework is not quite complete is that it assumes that the reward is
7:50
given by the environment you see this picture the agent sends an action while
7:56
the reward sends it an observation in a both the observation and the reward backwards that's what the environment
8:01
communicates back the way in which this is not the case in the real world is that we figure out
8:11
what the reward is from the observation we reward ourselves we are not told
8:16
environment doesn't say hey here's some negative reward it's our interpretation over census that lets us determine what
8:23
the reward is and there is only one real true reward in life and this is
8:28
existence or nonexistence and everything else is a corollary of that so well what
8:35
should our agent be you already know the answer should be a neural network because whenever you want to do
8:41
something dense it's going to be a neural network and you want the agent to map observations to actions so you let
8:47
it be parametrized with a neural net and you apply learning algorithm so I want to explain to you how reinforcement
8:53
learning works this is model free reinforcement learning the reinforcement learning has actually been used in practice everywhere but it's