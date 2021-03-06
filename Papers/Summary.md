# Summary of the papers:
## Continuous Control with Deep RL:
* Uses DPG(Deterministic Policy Gradient)
* Other techniques such as Experience Replay, Target Network and Batch Update
* Creates copy of both Actor(q') and Critic(pi') network
* Soft Update in target network
* Batch norm

*A deep RL framework for solving continious control problems using DPG.*

## Cooperative Inverse RL:
* Model based algorithm
* Inverse RL(IRL): Estimate the reward function from demontration and try to maximize it. Usually a model based algorithm.
* Cooperative IRL(CIRL): Cooperative game of a human and robot where only human *knows* the *reward function*. By observing the human, robot estimates the reward and takes action which will help it to maximize the sum of rewards.
* Apprenticeship Learning(ACIRL): Can be modelled as a CIRL game with two phases:
  * Learning Phase: Only human takes action
  * Deployment Phase: Only robot takes action
* Expert demonstration is generally a sub-optimal strategy in CIRL. 
* CIRL can be reduced to POMDP and the robot's posterior over reward is the sufficient statistic.

*Opposed to robot estimating reward function of human and adopting as its own, this paper presents a framework where robot knows that it is in a shared environment and attempts to maximize the human's reward. This helps in creating a cooperative learning behaviour.*

## Human-level performance in 3D multiplayer games with population-based RL:
* Concurrently trains different types of agents which play against each other.
* Each agent evolves its own internal dense reward signal based on available game points signal. 
* Modelled as two tier RL problem. Internal reward signals are maximized using Actor-Critic algorithms. Outer optimization of winning with respect to of internal reward model is performed through population based optimization.
* State representation is obtained through RNNs.

*Training a huge number of agents concurrently to achieve human level performance in FPS games.*

## On the Utility of Learning about Humans for Human-AI Coordination:
*In training for cooperative games using AI, we should include human models. Self-play or imitation can fail drastically in such scenarios.*

## An Efficient, Generalized Bellman Update For Cooperative Inverse Reinforcement Learning:
* Exponential redction in the size of action space for CIRL.
* Relax the assumption of human rationality

## Maximum Entropy Inverse Reinforcement Learning
* Model reward function as a linear features of states
* Get the gradient of Maximum Likelihood of the reward, and maximize it using Gradient Descent

## Shared Autonomy via Deep RL
* Shared Action space based end-to-end model free human in the loop RL framework
* Pre-trained agent. Final action depends on the agent.
* Agent let human take action if value is close to the optimal value.
