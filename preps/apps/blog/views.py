from django.views.generic import dates
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from preps.apps.blog.models import Post

class PostList(ListView):
    '''
    Defines a function which provides a list view of blog posts.
    '''
    # Let's return a variable to the template called "posts" to loop through.
    context_object_name = "posts"
    
    # Let's limit this to only active posts.
    queryset = Post.objects.filter(active=True).select_related()
    
    # Let's pick the blog/post_list template for this view.
    template_name = 'blog/post_list.html'
    
class PostDetail(DetailView):
    '''
    Defines a function which provides a detail view of blog posts.
    '''
    
    # Let's return a variable to the template called "post."
    context_object_name = "post"
    
    # Let's point at the Post model.
    model = Post
    
    # Time to override the get_queryset function to find our one post.
    def get_queryset(self):
        '''
        Defines a function which returns a queryset to build the detail view from.
        '''
        # Let's return only the post which matches on id (pk from the URL) and slug (slug from the URL).
        return Post.objects.filter(id=self.kwargs['pk'], slug=self.kwargs['post_slug'])
    
