import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: MyApp(),
  ));
}
// Stateful just means remembering whats going on
// Stateful Widget itself is not actually the state

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  createState() => _State();
}

class _State extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar: AppBar(
        title: Text('Name Here'),
      ),
      body: Container(
        padding: EdgeInsets.all(32.0),
        child: Center(
          child: Column(
            children: <Widget>[
              Text('Images Demo'),
              Expanded(child:
                Image.asset('Images/ElasticLoadBalancingandAuto_ScalingAWS.png'),
              ),
              Expanded(child:
                Image.network('https://d2908q01vomqb2.cloudfront.net/c5b76da3e608d34edb07244cd9b875ee86906328/2021/03/26/SmartStream-TLM-On-Demand-Architecture-on-AWS.png'),
              )
            ],
          ),
        ),
      ),
    );
  }
}
