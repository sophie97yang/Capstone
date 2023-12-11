import "./Footer.css";

function Footer() {

  return (
    <footer>
      <div id="footer-left">
      </div>

      <div id="footer-center">
        <p>This site was made with love by a travel lover, Sophie Yang </p>
        <a href="https://github.com/sophie97yang"><i className="fa-brands fa-square-github fa-2xl"></i></a>
        <a href="https://www.linkedin.com/in/sophie-yang-bb9758156/"><i className="fa-brands fa-linkedin fa-2xl" style={{ color: "#0047c2" }}></i></a>
        <p>&copy; {new Date().getFullYear()} SplitTrip, Inc. All Rights Reserved. Terms, Privacy & Accessibility
        </p>

      </div>


      <div id="footer-right">
      </div>
    </footer>
  );
}

export default Footer;
