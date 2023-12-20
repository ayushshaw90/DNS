import '../styles/globals.css';
import Layout from '../Components/Layout';
import Navbar from '../Components/Navbar';



export default function App({ Component, pageProps }) {
 
  
  return (

    <Layout>
      <div className={"pl-48 pr-8 pt-4 scroll-behavior-smooth" }>
        
        <Component {...pageProps}/>
        
      </div>
    </Layout>
    
  )
}