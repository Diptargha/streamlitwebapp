def html_aboutme_template():
    """html and css template to connect with me through linkedin, facebook and github"""
    about_me_template = """
    
    <!-- CSS  --> 
    <link 
    href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> <link 
    href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" 
    rel="stylesheet" media="screen,projection"/> <link href="static/css/style.css" type="text/css" rel="stylesheet" 
    media="screen,projection"/> <link rel="stylesheet" 
    href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" 
    integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous"> 
    <footer class="page-footer grey darken-4"> <div class="container" id="aboutapp"> <div class="row"> <div 
    class="col l6 s12"> <h5 class="white-text">Data Explorer App</h5> <p class="grey-text 
    text-lighten-4">Using Streamlit, Plotly, Seaborn and SweetViz.</p> </div> 
              
           <div class="col l3 s12">
                  <h5 class="white-text">Connect With Me</h5>
                  <ul>
                    <a href="https://www.facebook.com/diptarghachakravorty/" target="_blank" class="white-text">
                    <i class="fab fa-facebook fa-4x"></i>
                  </a>
                  <a href="https://www.linkedin.com/in/diptargha-chakravorty-20481a6b/" target="_blank" class="white-text">
                    <i class="fab fa-linkedin fa-4x"></i>
                  </a>
                   <a href="https://github.com/Diptargha/" target="_blank" class="white-text">
                    <i class="fab fa-github-square fa-4x"></i>
                  </a>
                  </ul>
                </div>
              </div>
            </div>
            <div class="footer-copyright">
          </footer>
        """

    return about_me_template
