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

  TextEditingController _user = TextEditingController();
  TextEditingController _pass = TextEditingController();

  // textfield is a gravy widget meaning if you dont specify size it'll keep expanding outward
  // obscure text is mechanism to hide text inputs for things ike passwords

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
            children: <Widget> [
              Text('Please Login'),
              Row(
              children: <Widget> [
                Text('Username'),
                Expanded(child: TextField(controller: _user)),
                // TextField(controller: _user,)
              ],
            ),
          Row(
            children: <Widget> [
              Text('Password'),
              Expanded(child: TextField(controller: _pass,obscureText: true,)),
              // TextField(controller: _user,)
            ],
          ),
              Padding(padding: EdgeInsets.all(12.0),
              child: ElevatedButton(
                  // ignore: avoid_print
                  onPressed: () => print('Login ${_user.text}'),
                  child: Text('Click me')
              )
              )
          ],
          ),
        ),
      ),
    );
  }
}
