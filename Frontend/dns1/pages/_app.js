import '../styles/globals.css';
import Layout from '../Components/Layout';
import Navbar from '../Components/Navbar';



export default function App({ Component, pageProps }) {
 
  
  return (

    <Layout>
      <div className={" scroll-behavior-smooth" }>
        
        <Component {...pageProps}/>
        
      </div>
    </Layout>
    
  )
}