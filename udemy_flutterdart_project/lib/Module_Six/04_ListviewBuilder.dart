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
              Card(
                child: Container(
                  padding: EdgeInsets.all(32.0),
                  child: Column(
                    children: <Widget> [
                    Text('Hello World'),
                    Text('How are you'),
                    ],
                  )
                )
              ),

              Card(
                  child: Container(
                      padding: EdgeInsets.all(32.0),
                      child: Column(
                        children: <Widget> [
                          Text('Hello World'),
                          Text('How are you'),
                        ],
                      )
                  )
              ),

              Card(
                  child: Container(
                      padding: EdgeInsets.all(32.0),
                      child: Column(
                        children: <Widget> [
                          Text('Hello World'),
                          Text('How are you'),
                        ],
                      )
                  )
              )

          ]
        ),
      ),
    )
    );
  }
}
