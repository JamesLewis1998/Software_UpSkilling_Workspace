import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: const Color.fromARGB(255, 58, 131, 183)),),
      home: const MyHomePage(
      title: 'Movie Marathon Series'),
    );
  }
}
      class MyHomePage extends StatefulWidget {
        const MyHomePage({super.key, required this.title});
        final String title;
        @override
        State<MyHomePage> createState() => _MyHomePageState();
      }

          class _MyHomePageState extends State<MyHomePage> {
            @override
            Widget build(BuildContext context) {
              return Scaffold(
                appBar: AppBar(
                    leading: Builder(
                                builder: (context){return IconButton(
                                icon: const Icon(Icons.menu),
                                onPressed: () {Scaffold.of(context).openDrawer();},
                                );
                            },
                      ),
                    title: Text(widget.title),
                    backgroundColor: Theme.of(context).colorScheme.inversePrimary,
                    actions: [ 
                      Padding(padding: const EdgeInsets.only(right: 8.0),
                      child: IconButton(onPressed: (){ Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const UAPage()),);
            }, icon: const Icon(Icons.movie)))
                      ,
                    ],
                ),

                drawer: Drawer(
                  child: ListView(
                  // Important: Remove any padding from the ListView.
                  padding: EdgeInsets.zero,
                  children: [
                    const DrawerHeader(
                      decoration: BoxDecoration(color: Colors.blue),
                      child: Text('Our Standouts'),
                    ),
                    ListTile(
                      title: const Text('Marvel Film Franchise'),
                      onTap: () {
                        // Update the state of the app.
                        // ...
                      },
                    ),
                    ListTile(
                      title: const Text('Starwars Film Franchise'),
                      onTap: () {
                        // Update the state of the app.
                        // ...
                      },
                    ),
                    ListTile(
                      title: const Text('Harry Potter Film Franchise'),
                      onTap: () {
                        // Update the state of the app.
                        // ...
                      },
                    ),
                  ],
                ),
                ),
                body: Center(
                  // Center is a layout widget. It takes a single child and positions it
                  // in the middle of the parent.
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: <Widget>[
                      const Text(
                        'Welcome to Movie Marathon Series, a website dedicated to providing the best movie line ups Film Franchises have to offer',
                      ),
                      
                    ],
                  ),
                ),
                
                );
            }
          }

class UAPage extends StatelessWidget {
  const UAPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('User Account Page'),
      actions: [ IconButton(onPressed: () { Navigator. pop(context);} , icon: Icon(Icons.arrow_back))],
        ),
      );
  }
}
