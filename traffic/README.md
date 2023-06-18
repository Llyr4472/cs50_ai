Traffic: Traffic Sign Identifier
Overview

Traffic is an AI project aimed at developing a sophisticated model for identifying traffic signs in photographs. Our goal is to create a high-performing AI system that can accurately recognize and classify various traffic signs, ultimately enhancing road safety and optimizing traffic management.
Dataset

For this project, we utilized a comprehensive dataset comprising a wide range of traffic sign images. To ensure thorough evaluation, we divided the dataset into two subsets: a small dataset for initial testing and parameter optimization, and a larger dataset for extensive evaluation.
Experimentation Process

During the development of the Traffic Sign Identifier, I engaged in a series of systematic experiments to determine the optimal parameters. Here's an insight into my thought process and the results obtained:

Using a Small Dataset for Testing:

In the initial phase, I focused on experimenting with the small dataset to establish a baseline for the model's performance.

Test1: I began by testing the model with 32 filters, a pool size of 3x3, 1 convolution and pooling layer, 64 hidden layer units, and a 50% dropout rate. This configuration resulted in an accuracy of 82.7%, indicating a promising start.

Test2: To further improve the model's accuracy, I increased the number of hidden layer units to 128 while keeping other parameters unchanged. This adjustment led to a remarkable accuracy of 100%, reflecting the model's ability to effectively learn and recognize traffic signs.

Using a Large Dataset for Testing:

With the insights gained from the small dataset experiments, I proceeded to evaluate the model's performance on a larger and more diverse dataset.

Test3: I maintained the same parameter settings as Test2, except for the hidden layer units, which remained at 128. The model achieved an impressive accuracy of 94.5%, demonstrating its capacity to generalize well to a broader range of traffic signs.

Test4: To explore the impact of additional convolution and pooling layers, I introduced a second set of convolution and pooling layers. While this modification increased the complexity, it slightly reduced the accuracy to 78.5%, suggesting a potential trade-off between complexity and accuracy.

Test5: Continuing the exploration, I experimented with adding an extra hidden layer. Surprisingly, this adjustment resulted in a noticeable drop in accuracy to 60.1%. It became apparent that excessively increasing model complexity without careful consideration could hinder performance.

Tests 6 to 11: During this phase, I thoroughly tested various combinations of parameters, including pool sizes, hidden layer configurations, and dropout rates. However, these experiments yielded suboptimal results, with accuracies ranging from 5.4% to 5.52%, highlighting the delicate balance required in parameter selection.

Identifying Optimal Parameters:

Test12: Inspired by the observation that the second set of convolution and pooling layers positively impacted accuracy in Test4, I decided to explore further by introducing two consecutive convolution layers followed by pooling layers. In this experiment, I used a pool size of 2x2 instead of 3x3. This adjustment significantly improved the accuracy to an impressive 97.4%. While the training time increased to 14 seconds per epoch, the substantial accuracy boost validated the effectiveness of this configuration.

Test13: To explore the impact of dropout rates, I reduced it to 12% while maintaining the same parameter settings as Test12. This adjustment sustained high accuracy, achieving an impressive 93.68%, further highlighting the model's ability to generalize well even with reduced regularization.

Test14: Similarly, I investigated the effects of a 25% dropout rate. The accuracy slightly decreased to 92.87%, suggesting a balanced trade-off between regularization and model complexity.
Conclusion

Based on the extensive experimentation, Test12, incorporating two consecutive convolution layers, a pool size of 2x2, 128 hidden layer units, and a 50% dropout rate, produced the best performance, achieving an accuracy of 97.4%. This configuration strikes a balance between complexity and accuracy, enabling the model to effectively identify and classify traffic signs.

It is important to note that these experiments were conducted on the larger dataset, ensuring robustness and generalization. The Traffic Sign Identifier developed through this project holds immense potential for real-world applications, contributing to safer roads and more efficient traffic management.

For further details, including parameter configurations, accuracy metrics, and the training process, please refer to the comprehensive log file available in the project repository.
