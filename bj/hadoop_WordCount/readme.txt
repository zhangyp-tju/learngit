----0
hadoop dfs -ls [folder_path]
hadoop dfs -ls 
hadoop dfs -ls yapeng/WC/input
hadoop dfs -mkdir yapeng/WC
hadoop dfs -copyToLocal yapeng/WC/output/* ./

[@sjs_37_33 hadoopwork]# echo "foo foo quux labs foo bar quux" | ./word_count_mapper.py | sort | ./word_count_ruducer.py 
bar	1
foo	3
labs	1
quux	2
hadoop dfs -mkdir yapeng/WC
# hadoop dfs -copyFromLocal 1.txt 2.txt yapeng/WC/input

----1Haoop支持用其他语言来编程，需要用到名为Streaming的通用API。Haoop支持用其他语言来编程，需要用到名为Streaming的通用API。
Streaming主要用于编写简单，短小的MapReduce程序，可以通过脚本语言编程，开发更快捷，并充分利用非Java库。
HadoopStreaming使用Unix中的流与程序交互，从stdin输入数据，从stdout输出数据。实际上可以用任何命令作为mapper和reducer。数据流示意如下：

cat [intput_file] | [mapper] | sort | [reducer] > [output_file]
----2
Hadoop Streaming的优缺点
优点
可以使用自己喜欢的语言来编写MapReduce程序（换句话说，不必写Java XD）
不需要像写Java的MR程序那样import一大堆库，在代码里做一大堆配置，很多东西都抽象到了stdio上，代码量显著减少
因为没有库的依赖，调试方便，并且可以脱离Hadoop先在本地用管道模拟调试
缺点
只能通过命令行参数来控制MapReduce框架，不像Java的程序那样可以在代码里使用API，控制力比较弱，有些东西鞭长莫及
因为中间隔着一层处理，效率会比较慢
所以Hadoop Streaming比较适合做一些简单的任务，比如用python写只有一两百行的脚本。如果项目比较复杂，或者需要进行比较细致的优化，使用Streaming就容易出现一些束手束脚的地方。
----3
在streaming程序中使用lzo压缩
把inputformat设置为DeprecatedLzoTextInputFormat，还要设置参数 stream.map.input.ignoreKey=true，
----4



