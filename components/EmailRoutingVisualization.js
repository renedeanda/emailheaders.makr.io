
import { useEffect, useRef } from 'react'
import * as d3 from 'd3'

export default function EmailRoutingVisualization({ receivedHeaders }) {
  const svgRef = useRef()

  useEffect(() => {
    if (!receivedHeaders || receivedHeaders === 'Not available') return

    const hops = receivedHeaders.split('\n').reverse()
    const nodes = hops.map((hop, index) => ({ id: index, name: hop.split(' ')[1] }))
    const links = nodes.slice(1).map((node, index) => ({ source: index, target: index + 1 }))

    const width = 600
    const height = nodes.length * 50

    const svg = d3.select(svgRef.current)
      .attr('width', width)
      .attr('height', height)

    const simulation = d3.forceSimulation(nodes)
      .force('link', d3.forceLink(links).id(d => d.id).distance(50))
      .force('charge', d3.forceManyBody().strength(-100))
      .force('center', d3.forceCenter(width / 2, height / 2))

    const link = svg.append('g')
      .selectAll('line')
      .data(links)
      .join('line')
      .attr('stroke', '#999')
      .attr('stroke-opacity', 0.6)
      .attr('stroke-width', 2)

    const node = svg.append('g')
      .selectAll('circle')
      .data(nodes)
      .join('circle')
      .attr('r', 5)
      .attr('fill', '#69b3a2')

    const text = svg.append('g')
      .selectAll('text')
      .data(nodes)
      .join('text')
      .text(d => d.name)
      .attr('font-size', 10)
      .attr('dx', 8)
      .attr('dy', 3)

    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y)

      node
        .attr('cx', d => d.x)
        .attr('cy', d => d.y)

      text
        .attr('x', d => d.x)
        .attr('y', d => d.y)
    })
  }, [receivedHeaders])

  return (
    <div className="mt-6">
      <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-200 mb-2">Email Routing Visualization</h3>
      <svg ref={svgRef}></svg>
    </div>
  )
}
