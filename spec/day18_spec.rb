# frozen_string_literal: true

require './day18'
using Refinements

# https://adventofcode.com/2021/day/17
RSpec.describe String do
  describe '#to_sn' do
    it 'correctly parses a snailfish number string' do
      sn_string = '[[1,2],3]'
      sn = sn_string.to_sn
      expect(sn.left.parent).to eq(sn)
      # 1
      expect(sn.left.left.parent).to eq(sn.left)
      expect(sn.left.left.left).to be_nil
      expect(sn.left.left.right).to be_nil
      expect(sn.left.left.value).to eq(1)
      # 2
      expect(sn.left.right.parent).to eq(sn.left)
      expect(sn.left.right.left).to be_nil
      expect(sn.left.right.right).to be_nil
      expect(sn.left.right.value).to eq(2)
      # 3
      expect(sn.right.parent).to eq(sn)
      expect(sn.right.left).to be_nil
      expect(sn.right.right).to be_nil
      expect(sn.right.value).to eq(3)
    end
  end
end

RSpec.describe SnailfishNumber do
  describe '#to_a' do
    it 'correctly renders a snailfish number as an array' do
      sn = '[[1,2],[[3,4],[5,6]]]'.to_sn
      expect(sn.to_a).to eq([[1, 2], [[3, 4], [5, 6]]])
    end
  end

  describe '#add' do
    it 'correctly adds two snailfish numbers' do
      sum = '[1,2]'.to_sn + '[[3,4],[[5,6],[7,8]]]'.to_sn
      expect(sum.to_a).to eq([[1,2],[[3,4],[[5,6],[7,8]]]])
      expect(sum.left.parent).to eq(sum)
    end
  end

  describe '#to_explode' do
    it 'correctly picks the first pair to explode' do
      example = '[[[[[9,8],1],2],3],4]'.to_sn
      expect(example.to_explode(0).to_a).to eq([9, 8])
      example = '[7,[6,[5,[4,[3,2]]]]]'.to_sn
      expect(example.to_explode(0).to_a).to eq([3, 2])
      example = '[[6,[5,[4,[3,2]]]],1]'.to_sn
      expect(example.to_explode(0).to_a).to eq([3, 2])
      example = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'.to_sn
      expect(example.to_explode(0).to_a).to eq([7, 3])
      example = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'.to_sn
      expect(example.to_explode(0).to_a).to eq([3, 2])
    end
  end
end
