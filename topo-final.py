from mininet.topo import Topo

class MyTopo( Topo ):


	def __init__( self ):

	# Initialize topology
		Topo.__init__( self )

		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		s1 = self.addSwitch( 's1' )
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		s4 = self.addSwitch( 's4' )
	

		# Adding links
		self.addLink( h1,s1)
		self.addLink( s1,s2 )
		self.addLink( s2,s3)
		self.addLink( s3,s4)
		self.addLink( s4,s1)
		#self.addLink( s1,s3 )
		self.addLink( s3,h2)



topos = { 'topo-final': ( lambda: MyTopo() ) }





