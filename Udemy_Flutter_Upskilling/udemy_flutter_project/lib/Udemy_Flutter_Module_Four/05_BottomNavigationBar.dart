import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: MyApp(),
  ));
}
class MyApp extends StatefulWidget {
  const MyApp({super.key});
  @override
  createState() => _State();
}

class _State extends State<MyApp> {
  late List<BottomNavigationBarItem> _items;
  String _value = '';
  int _index = 0;
  @override
  void initState() {
    _items =  [];
      _items.add(BottomNavigationBarItem(
          icon: Icon(Icons.people),
          label: 'People',));
    _items.add(BottomNavigationBarItem(
      icon: Icon(Icons.weekend),
      label: 'Weekend',));
   _items.add(BottomNavigationBarItem(
      icon: Icon(Icons.message),
      label: 'Message',));



  }
  // initial state is - before anything is rendered on the screen for
  // the first time what do we want to do with our state
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
              Text('Hello World')
            ],
          ),
        ),
      ),
      
      bottomNavigationBar: BottomNavigationBar(
          items: _items,
        fixedColor: Colors.blue,
        currentIndex: _index,
        onTap: (int item){
            setState(() {
              _index = item;
              _value = 'Current Value is: ${_index.toString()}';
            });
        },
      ),
      // Now we have a fully functional bottom navigation bar :)
    );
  }
}