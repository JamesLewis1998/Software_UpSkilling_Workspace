import 'package:flutter/material.dart';

class MovieSearchDel extends SearchDelegate{

      @override
      Widget? buildLeading(BuildContext context) => IconButton(
        onPressed: () => close(context, null), 
        icon: const Icon(Icons.arrow_back));
      
      @override
      List<Widget>? buildActions(BuildContext context) => [IconButton(
        icon: const Icon(Icons.clear),
        onPressed: (){ 
          if (query.isEmpty){close(context, null);} 
          else {query= '';} },),];
      
      @override
      Widget buildResults(BuildContext context) => Container();
        @override
        void showResults(BuildContext context) {
          Navigator.of(context).popAndPushNamed('/rro',arguments:query,);
          super.showResults(context);
        }

      @override
      Widget buildSuggestions(BuildContext context) {
        final suggestionList = query.isEmpty;

        return ListView.builder(itemBuilder: (context,index)=> ListTile(
          onTap: (){
            Navigator.of(context).pushNamed('/rro',arguments: query);
          },
        ),
        );
      }
}